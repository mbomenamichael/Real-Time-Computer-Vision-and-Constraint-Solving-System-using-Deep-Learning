import cv2
import numpy as np
import operator
from keras.models import load_model
import sudoku_solver as sol
import time

classifier = load_model("digit_model.h5")

margin = 4
cell = 28 + 2 * margin
grid_size = 9 * cell

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
flag = 0
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1080, 620))

while True:
    start_time = time.time()
    process_start_time = time.time()  # start time of the process
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 2)

    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    grid_contour = None
    maxArea = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area > 25000:
            peri = cv2.arcLength(c, True)
            polygon = cv2.approxPolyDP(c, 0.01 * peri, True)
            if area > maxArea and len(polygon) == 4:
                grid_contour = polygon
                maxArea = area

    if grid_contour is not None:
        cv2.drawContours(frame, [grid_contour], 0, (0, 255, 0), 2)
        points = np.vstack(grid_contour).squeeze()
        points = sorted(points, key=operator.itemgetter(1))

        if points[0][0] < points[1][0]:
            if points[3][0] < points[2][0]:
                pts1 = np.float32([points[0], points[1], points[3], points[2]])
            else:
                pts1 = np.float32([points[0], points[1], points[2], points[3]])
        else:
            if points[3][0] < points[2][0]:
                pts1 = np.float32([points[1], points[0], points[3], points[2]])
            else:
                pts1 = np.float32([points[1], points[0], points[2], points[3]])

        pts2 = np.float32([[0, 0], [grid_size, 0], [0, grid_size], [grid_size, grid_size]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        grid = cv2.warpPerspective(frame, M, (grid_size, grid_size))
        grid = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
        grid = cv2.adaptiveThreshold(grid, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 7, 3)

        cv2.imshow("grid", grid)

        if flag == 0:
            grid_txt = []
            for y in range(9):
                line = ""
                for x in range(9):
                    y2min = y * cell + margin
                    y2max = (y + 1) * cell - margin
                    x2min = x * cell + margin
                    x2max = (x + 1) * cell - margin

                    cv2.imwrite("mat" + str(y) + str(x) + ".png",
                    grid[y2min:y2max, x2min:x2max])
                    img = grid[y2min:y2max, x2min:x2max]
                    img_reshaped = img.reshape(1, 28, 28, 1)
                    if img_reshaped.sum() > 10000:
                        prediction = np.argmax(classifier.predict(img_reshaped), axis=-1)
                        line += "{:d}".format(prediction[0])
                    else:
                        line += "{:d}".format(0)
                grid_txt.append(line)
            print(grid_txt)
            result = sol.sudoku(grid_txt)
            print("Result:", result)
        
    
        if result is not None:
            flag = 1
            background = np.zeros(
                shape=(grid_size, grid_size, 3), dtype=np.float32)
            for y in range(len(result)):
                for x in range(len(result[y])):
                    if grid_txt[y][x] == "0":
                        cv2.putText(background, "{:d}".format(result[y][x]), ((
                            x) * cell + margin + 3, (y + 1) * cell - margin - 3), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, (0, 0, 255), 1)
            M = cv2.getPerspectiveTransform(pts2, pts1)
            h, w, c = frame.shape
            backgroundP = cv2.warpPerspective(background, M, (w, h))
            img2gray = cv2.cvtColor(backgroundP, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
            mask = mask.astype('uint8')
            mask_inv = cv2.bitwise_not(mask)
            img1_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            img2_fg = cv2.bitwise_and(backgroundP, backgroundP, mask=mask).astype('uint8')
            dst = cv2.add(img1_bg, img2_fg)
            dst = cv2.resize(dst, (1080, 620))
            cv2.imshow("frame", dst)
            out.write(dst)

        else:
            frame = cv2.resize(frame, (1080, 620))
            cv2.imshow("frame", frame)
            out.write(frame)

    else:
        flag = 0
        frame = cv2.resize(frame, (1080, 620))
        cv2.imshow("frame", frame)
        out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Calculates and display FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time)
    
    if grid_contour is not None and result is not None:
        cv2.putText(dst, "FPS : " + str(int(fps)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("frame", dst)
        out.write(dst)
    else:
        cv2.putText(frame, "FPS : " + str(int(fps)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        frame = cv2.resize(frame, (1080, 620))
        cv2.imshow("frame", frame)
        out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
 # times how long it takes to solve the sudoku from when it it recognised
    if grid_contour is not None and result is not None:
        process_end_time = time.time()  # end time of the process
        print("Process time : " + str(process_end_time - process_start_time) + " seconds")  # print the process time
        cv2.putText(dst, "Process time : " + str(process_end_time - process_start_time) + " seconds", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("frame", dst)
        out.write(dst)

out.release()
cap.release()
cv2.destroyAllWindows()
