let time = readline().split(" ");

function fixTime(time) {
    let hour = parseInt(time[0]);
    let minute = parseInt(time[1]);
    if (minute >= 45) {
        return hour + " " + (minute - 45);
    }
    if (hour === 0) {
        hour = 23;
    } else {
        hour--;
    }
    return hour + " " + (minute - 45 + 60);
}
print(fixTime(time));